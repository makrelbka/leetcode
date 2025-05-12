func maxDistToClosest(seats []int) int {
    len_s := len(seats)
    cnt := 0
    maxx := 0
    i := 0
    for {
        if i >= len_s {
            break
        }
        if seats[i] == 1 {
            break
        } else {
            maxx++
        }
        i++
    }
    fmt.Println(maxx)
    for {
        if i >= len_s {
            break
        }
        if seats[i] == 1 {
            maxx = max(maxx, cnt)
            cnt = 0
        } else {
            cnt++
        }
        i++
    }
    if maxx % 2 == 0 {
        maxx = maxx / 2
    } else {
        maxx = maxx / 2 + 1
    }

    maxx = max(maxx, cnt)


    i = 0
    cnt = 0
    for {
        if i >= len_s {
            break
        }
        if seats[i] == 1 {
            break
        } else {
            cnt++
        }
        i++
    }
    maxx = max(maxx, cnt)

    return maxx
}


/*
Maximize Distance to Closest Person:
Идем сначала ищем максимумальную последовательность из нулей, найденный результат поделим на 2 чтобы найти расстояние до ближайшего
Теперь отдельно посмотрим на последнюю итерацию, ее не надо делить на 2 так как человек может сесть скраю
И запустим алгоритм еще раз, чтобы посмотреть такой же случай если человек сядет с краю в начале 
*/