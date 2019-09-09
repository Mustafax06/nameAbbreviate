package main

import (
	"fmt"
	"strings"
)

func abbreviateName(fullName string, fNameStatement bool, mNameStatement bool, sNameStatement bool) {
	slicedFullName := strings.Split(fullName, " ")
    midNames := slicedFullName[:len(slicedFullName)-1]
	midNames = midNames[1:]
	output := ""
	dot := "."
	space := " "

	if fNameStatement == true {
		output += string(slicedFullName[0][0]) + dot + space
	}

	if len(midNames) > 1 {
		if mNameStatement == true {
			for i, s := range midNames {
				output += string(s[i-i]) + "." + " "
			}
		}
	}

	if sNameStatement == true {
		output += string(slicedFullName[len(slicedFullName)-1][0]) + dot + space
	}

	fmt.Println(output)
}

func main() {
	abbreviateName("Mustafa Samir Veli Dili", true, true, true)
}
