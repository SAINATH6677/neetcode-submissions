class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>m;
        string s = "";
        for(int i=0;i<strs.size();i++){
            s = strs[i];
            sort(s.begin(),s.end());
            m[s].push_back(strs[i]);
        }
        vector<vector<string>> res;
        for(auto& p : m){
            res.push_back(p.second);
        }
        return res;
    }
};
