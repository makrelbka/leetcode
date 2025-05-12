type MyQueue struct {
    st *Node
    en *Node  
}

type Node struct {
    left *Node 
    right *Node 
    value int
}


func Constructor() MyQueue {
    return MyQueue{nil, nil}
}


func (this *MyQueue) Push(x int)  {
    if (this.st == nil) {
        node := Node{nil, nil, x}
        this.st = &node
        this.en = &node
    } else {
        node := Node{nil, this.st, x}
        this.st.left = &node
        this.st = &node
    }
}


func (this *MyQueue) Pop() int {
    res := this.en.value
    
    if this.en.left == nil {
        this.st = nil
        this.en = nil
    } else {
        this.en = this.en.left 
    }
    return res
}


func (this *MyQueue) Peek() int {
    return this.en.value
}


func (this *MyQueue) Empty() bool {
    return this.st == nil
}


/*
Implement Queue using Stacks
Просто очередь на линкт листе 
 */