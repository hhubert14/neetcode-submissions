class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        int[] start_times = new int[intervals.size()];
        int[] end_times = new int[intervals.size()];
        for (int i = 0; i < intervals.size(); i++) {
            start_times[i] = intervals.get(i).start;
            end_times[i] = intervals.get(i).end;
        }
        Arrays.sort(start_times);
        Arrays.sort(end_times);
        int i = 0;
        int j = 0;
        int ans = 0;
        while (i < intervals.size() && j < intervals.size()) {
            while (i < intervals.size() && start_times[i] < end_times[j]) {
                i++;
            }
            ans = Math.max(i-j, ans);
            j++;
        }
        return ans;
    }
}