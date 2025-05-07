func longestOnes(nums []int, k int) int {
    maxCons := 0
    st := 0
    en := -1
    l := len(nums)
    for en < l - 1  {
        if k > 0 {
            en++
            if nums[en] == 0 {
                k--
            }
        } else {
            if en < l && nums[en + 1] == 1{
                en++
                continue
            }
            maxCons = max(maxCons, en - st + 1)
            if nums[st] == 0 {
                k++
            } 
            st++
        } 
    }
    maxCons = max(maxCons, en - st + 1)
    return maxCons
}
