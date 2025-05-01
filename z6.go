func convert(s string, numRows int) string {
	if numRows == 1 {
		 return s
	 }
 
	 step := 2*numRows - 2
	 arr := make([]strings.Builder, numRows)
 
	 for i, ch := range s {
		 idx := i % step
		 if idx >= numRows {
			 idx = step - idx
		 }
		 arr[idx].WriteRune(ch) 
	 }
 
	 var res strings.Builder
	 for _, sb := range arr {
		 res.WriteString(sb.String())
	 }
	 
	 return res.String()
 }