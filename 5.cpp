#include <bits/stdc++.h>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;

    for (int num : nums) {
        freq[num]++;
    }

    // Max Heap: pair<frequency, element>
    priority_queue<pair<int, int>> pq;

    for (auto it : freq) {
        pq.push({it.second, it.first});
    }

    vector<int> result;

    // Get top k elements
    while (k--) {
        result.push_back(pq.top().second);
        pq.pop();
    }

    return result;
}

int main() {
    vector<int> nums = {1,2,2,3,3,3};
    int k = 2;
    vector<int> ans = topKFrequent(nums, k);
    for (int x : ans) cout << x << " ";
}