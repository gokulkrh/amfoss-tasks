package main

import(
	"flag"
	"github.com/amit-lulla/twitterapi"
	"encoding/json"
	"os"
)

func main() {
	handlePtr := flag.String("handle", "abcd", "twitterhandle")
	flag.Parse()
	twitterapi.SetConsumerKey("nKPuhKiV3FqFrVJIJ7BUOjZ5p")
	twitterapi.SetConsumerSecret("hGjqN4RK4h0WmSNZEK9YNFtWofmxJYQUYIo2Eftk3B5inMmGmK")
	api := twitterapi.NewTwitterApi("1208336848734474241-L7JqxgpCSQsRqiLX0kKVk5wglwjCmj", "06hPj2H70ZimYjB0ONr7q0YWZuWHgRFPx0kNoO545aCFG")
	
	var data twitterapi.User
	data, _ = api.GetUsersShow(*handlePtr, nil)
	details, _ := json.MarshalIndent(data, "", " ")
	
	fo, _ := os.Create("./userinfo.txt")
	fo.WriteString(string(details))
	fo.Close()
}