/*

Cheetah - HQ9+ REPL written in Go

Beta 2 | PRODUCTION UN-READY

12/7/2021
David Costell

*/

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func isvalid(list string) bool {
	// Used to check if input is valid
	switch list {
	case
		"H",
		"Q",
		"9",
		"+",
		"help",
		"exit":
		return true
	}
	return false
}

func main() {

	scanner := bufio.NewScanner(os.Stdin) // Initialize scanner
	accumulator := 0                      // Accumulator

	fmt.Println("Cheetah - HQ9+ REPL in Go")
	fmt.Println("Version BETA 2 | 12/7/2021")
	fmt.Println("Type 'help' to display help." + "\n")

	for {
		fmt.Printf("HQ9+ >> ")
		scanner.Scan() // Get input
		input := scanner.Text()

		// Input Parser
		if isvalid(input) {

			if input == "H" {
				// Hello, World!
				fmt.Println("Hello, World!" + "\n")
			}
			if input == "Q" {
				// Quine (single Q)
				fmt.Println("Q" + "\n")
			}
			if input == "9" {
				// 99 Bottles of Beer
				bottles := func(num int) string {
					switch num {
					case 0:
						return "no more bottles"
					case 1:
						return "1 bottle"
					default:
						return fmt.Sprintf("%d bottles", num)
					}
				}
				for i := 99; i > 0; i-- {
					fmt.Printf("%s of beer on the wall, ", bottles(i))
					fmt.Printf("%s of beer. \n", bottles(i))
					fmt.Printf("Take one down, pass it around, %s of beer on the wall. \n", bottles(i-1))
					fmt.Println()
				}
				fmt.Println("No more bottles of beer on the wall, no more bottles of beer.")
				fmt.Println("Go to the store and buy some more, 99 bottles of beer on the wall." + "\n")
			}
			if input == "+" {
				// Accumulator
				accumulator++
				fmt.Println("Accumulator incremented." + "\n")
			}

			if input == "help" {
				// Help
				fmt.Println("Cheetah REPL - Help:")
				fmt.Println("Instructions are case-sensitive." + "\n")
				fmt.Println("H - Hello, World!")
				fmt.Println("Q - Quine")
				fmt.Println("9 - 99 Bottles of Beer")
				fmt.Println("+ - Increment Acccumulator")
				fmt.Println("help - Displays this help prompt.")
				fmt.Println("exit - Exits the program." + "\n")
			}
			if input == "exit" {
				// Exit program
				os.Exit(0)
			}

		} else {
			if strings.Contains(input, "Q") {
				// Quine (multiple Qs)
				quine := input + "\n"
				final := strings.Repeat(quine, strings.Count(quine, "Q"))
				fmt.Println(final)
			} else {
				// Invalid input
				fmt.Println("Invalid instruction." + "\n")
			}
		}

	}
}
