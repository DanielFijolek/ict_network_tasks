#include<iostream>
#include<filesystem>
#include<string>
#include<vector>
#include<cmath>
#include<sstream>
#include <fstream>
namespace fs = std::filesystem;
using namespace std;
template<class T> char* as_bytes(T& i)
{
	void* addr = &i;
						
	return static_cast<char*>(addr); 
}

struct Pack{
    uint8_t index;
    uint8_t lenght;
};

void pack(){
  string filename = "text.txt";
  fstream ifs (filename,std::ios::binary|std::ios::in);
  unsigned int data_size = 4;
  auto file_size = fs::file_size(filename);
  vector<uint8_t*> data_pack;
  
  for(long long id = 0; id <=ceil(file_size/data_size);id++){
  
    uint8_t * buffer;
    buffer = new uint8_t[sizeof(Pack) + data_size * sizeof(uint8_t)];
    Pack* SP1 = (Pack*)buffer;
    char * d = (char*)(SP1 + 1);
    unsigned int len = data_size;
    

    for(int i = 0; i < data_size; i++ ){
      uint8_t x;
      if(ifs.read(as_bytes(x), sizeof(uint8_t))){
          d[i] = x;
        } else{
          len = i;
          for(i;i<data_size;i++){
            d[i] = 0;
          }
        }
      }
    Pack* temp_pack = new (SP1) Pack;
    
    temp_pack->index = id;
    cout << id << " ";
    if (len == data_size){
      temp_pack->lenght = data_size;
      cout << data_size << " ";
    }else{
      temp_pack->lenght = len;
      cout << len << " " ;
    }
    cout << d << " ";
    cout << buffer << endl;
    data_pack.push_back(buffer);
    
  }

}

int main() {
  pack();
  return 0;
}