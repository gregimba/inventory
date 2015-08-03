package main

import "fmt"
import "os"

type item struct {
	id int
	name string
	description string
	quantity int
	location string
}

func main() {
		args := os.Args[1]

		switch args {
		case "list":
				fmt.Println("List current args")
		case "create":
				fmt.Println("create a new item")
		case "read":
				fmt.Println("look at a specific item")
		case "update":
				fmt.Println("change an item")
		case "delete":
				fmt.Println("delete an item")
		default:
				fmt.Println("Options include list, create, read, update, delete")
		}

}
