#include<iostream>
#include <vector>
using namespace std;

struct p_cb
{
    int id;
    int pcb_size;
};
struct memory
{
    int number;  //序号
    int front_number;  //前一个的序列号
    int id;  //占用程序的id 0为未占用
    bool flag;//0为未被占用
    int M_size; //大小
};

p_cb pc1={1,130};
p_cb pc2={2,60};
p_cb pc3={3,100};
p_cb pc4={4,200};
p_cb pc5={5,140};
p_cb pc6={6,60};
p_cb pc7={7,50};
struct memory M[2]={
    {0,0,0,1,0},
    {640,0,0,0,640}
};
vector<memory> M_queue;
memory temp;
vector<memory> best_queue;
int chose;
void M_merge(int mer_id)  //合并
{
    if((mer_id<M_queue.size()-1)&&(M_queue[mer_id+1].flag==0))
    {
        M_queue[mer_id+1].M_size+=M_queue[mer_id].M_size;
        M_queue[mer_id+1].front_number=M_queue[mer_id].front_number;
        M_queue.erase(M_queue.begin()+mer_id);
    }
    else{}
    if(M_queue[mer_id-1].flag==0)
    {
        M_queue[mer_id].M_size+=M_queue[mer_id-1].M_size;
        M_queue[mer_id].front_number=M_queue[mer_id-1].front_number;
        M_queue.erase(M_queue.begin()+mer_id-1);
    }
    else {}
}
void M_print()
{   cout<<"-----------------------------------"<<endl;
    cout<<"last num\tnum\tID\tsize\tlabel"<<endl;
    for(int i=1;i<M_queue.size();i++)
    {
        cout<<M_queue[i].front_number<<"\t"<<M_queue[i].number<<"\t"<<M_queue[i].id<<"\t"<<M_queue[i].M_size<<"\t\t"<<M_queue[i].flag<<endl;
    }
    cout<<"-----------------------------------"<<endl;
    cout<<endl<<endl;
}
void alloc(p_cb p1)
{
    if(chose==1)   //首次适应算法
    {
        for(int i=0;i<M_queue.size();i++)
        {
            if((M_queue[i].flag==0)&&p1.pcb_size<M_queue[i].M_size)
            {
                temp.flag=1;
                temp.id=p1.id;
                temp.front_number=M_queue[i].front_number;
                temp.M_size=p1.pcb_size;
                temp.number=M_queue[i].front_number+p1.pcb_size;
                M_queue[i].front_number=temp.number;
                M_queue[i].M_size-=p1.pcb_size;
                M_queue.insert(M_queue.begin()+i,temp);
                break;

            }
        }

    }
    else if(chose==2)   //最佳适应算法
    {
        int best_num=640;
        int best_i;
        for(int i=0;i<M_queue.size();i++)
        {
            if((M_queue[i].flag==0)&&(M_queue[i].M_size>=p1.pcb_size)&&(M_queue[i].M_size<=best_num))
            {
                best_num=M_queue[i].M_size;
                best_i=i;
            }
        }
        temp.flag=1;
        temp.id=p1.id;
        temp.front_number=M_queue[best_i].front_number;
        temp.M_size=p1.pcb_size;
        temp.number=M_queue[best_i].front_number+p1.pcb_size;
        M_queue[best_i].front_number=temp.number;
        M_queue[best_i].M_size-=p1.pcb_size;
        M_queue.insert(M_queue.begin()+best_i,temp);


    }
    else{

    }

    M_print();
}
void free(p_cb p2)
{   int id;
    for(int i=0;i<M_queue.size();i++)
    {

        if(p2.id==M_queue[i].id)
        {
            M_queue[i].flag=0;
            M_queue[i].id=0;
            id=i;
            break;
        }
    }
    M_merge(id);
    M_print();

}

int main()
{

    M_queue.push_back(M[0]);
    M_queue.push_back(M[1]);
    best_queue.assign(M_queue.begin(),M_queue.begin()+M_queue.size());
    cout<<"1 First Fit\n2 Best Fit\nInput:";
    cin>>chose;

    if(chose!=1&&chose!=2)
    {
        cout<<"error"<<endl;
    }

    cout<<"alloc(process[1])"<<endl;
    alloc(pc1);

    cout<<"alloc(process[2])"<<endl;
    alloc(pc2);

    cout<<"alloc(process[3])"<<endl;
    alloc(pc3);

    cout<<"free(process[2])"<<endl;
    free(pc2);

    cout<<"alloc(process[4])"<<endl;
    alloc(pc4);

    cout<<"free(process[3])"<<endl;
    free(pc3);

    cout<<"free(process[1])"<<endl;
    free(pc1);

    cout<<"alloc(process[5])"<<endl;
    alloc(pc5);

    cout<<"alloc(process[6])"<<endl;
    alloc(pc6);

    cout<<"alloc(process[7])"<<endl;
    alloc(pc7);

    cout<<"free(process[6])"<<endl;
    free(pc6);

    return 0;
}
