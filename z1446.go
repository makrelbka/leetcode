func maxPower(s string) int {
    l := 0
    r := 0
    cnt := 0
    len_s := len(s)

    for r < len_s {
        if s[l] != s[r] {
            cnt = max(cnt, r - l)
            l = r
        }
        r++
    }
    cnt = max(cnt, r - l)
    return cnt
}

/*
Consecutive Characters
Идем двумя указателями по строке
Двигаем правый пока значение по нему равно значению по левому
В ином случае обновляем максимум и передиваем левый указатель к правому 
*/