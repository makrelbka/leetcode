func removeElement(nums []int, val int) int {
    l := len(nums)
    end := 0
    for i := 0; i < l; i++ {
        if (nums[i] != val) {
            nums[end], nums[i] = nums[i], nums[end]
            end++
        }
    }
    return end 
}