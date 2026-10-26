class MinStack {
private:
        vector<pair<int,int>> stack;

public:
    MinStack() {
    }
    
    void push(int val) {
        if (stack.empty()) {
            stack.push_back({val,val});
        }
        else {
            int cur_min=stack.back().second;
            stack.push_back({val,min(val,cur_min)});
        }
    }
    
    void pop() {
        if (!stack.empty()) stack.pop_back();

        
    }
    
    int top() {
        if (!stack.empty()) return stack.back().first;

        return -1;
    }
    

    int getMin() {
        if (!stack.empty()) return stack.back().second;

        return -1;
    }
    
};
