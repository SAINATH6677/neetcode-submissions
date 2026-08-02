class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int a = 0;
        for(int num : nums){
            if(num == 1){
                a++;
                ans = max(ans,a);
            }
            else{
                a = 0;
            }
        }
        return ans;
    }
};