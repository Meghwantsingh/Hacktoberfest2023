#include<stdio.h>
#include<stdlib.h>
struct node{
    int data;struct node *next;
};
void insert(struct node **Node,struct node **rear,int item)
{
    
    struct node *ptr=(struct node*)malloc(sizeof(struct node));
    ptr->data=item;
    if(*Node==NULL)
    {
        *Node=ptr;
  
    }
    else{
        (*rear)->next=ptr;
         
    }
     ptr->next=NULL;
     *rear=ptr;
}
void traversal(struct node *head)
{
    struct node *temp=head;
    
    printf("%d ",temp->data);
    temp=temp->next;
    while(temp!=head)
    {
        printf("%d ",temp->data);
        temp=temp->next;
    }
}
int calculate(struct node *head,int k)
{
    struct node *temp=head;
    struct node *prev=head;
    int i;
    while(temp->next!=temp)
    {
        for(i=0;i<k-1;i++){
            prev=temp;
            temp=temp->next;
        }
        prev->next=temp->next;
        temp=prev->next;
        
        
    }
    return temp->data;
}
int main()
{
    struct node *Node=NULL;
    struct node *rear=NULL;
    int option;
    while(1)
    {
        printf("Enter 0.Stop 1.Entry\n");
        scanf("%d",&option);
        if(option==1)
        {
            int item;
            printf("Enter ");
            scanf("%d",&item);
            insert(&Node,&rear,item);
            
            
        }
        else
        {
            rear->next=Node;
            traversal(Node);
            int show=calculate(Node,3);
            printf("%d",show);
            break;
        }
    }
}
