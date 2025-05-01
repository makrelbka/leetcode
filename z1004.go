package main

import (
    "fmt"
)

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

func main() {
    nums1 := []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0}
    k1 := 2
    fmt.Println(longestOnes(nums1, k1)) 
    nums2 := []int{0,0,0,1}
    k2 := 4
    fmt.Println(longestOnes(nums2, k2))
}