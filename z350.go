func intersect(nums1 []int, nums2 []int) []int {
    sort.Ints(nums1)
    sort.Ints(nums2)

    i1:=0
    i2:=0
    var res []int
    for i1 < len(nums1) && i2< len(nums2) {
        if (nums1[i1] == nums2[i2]) {
            res = append(res, nums1[i1])
            i1++
            i2++
        } else if nums1[i1] > nums2[i2]{
            i2++
        } else {
            i1++
        }
    }
    return res

}

/*
Intersection of Two Arrays II
Сортируем оба массива 
Идем указателем по каждому из массивов
Если элементы равны то записывем в массив результата этот элемент и увеличиваем оба указателя
Иначе увеличиваем указатель того массива чей элемент меньше 
*/