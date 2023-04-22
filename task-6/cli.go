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
	twitterapi.SetConsumerKey("consumerkey")
	twitterapi.SetConsumerSecret("consumersecret")
	api := twitterapi.NewTwitterApi("", "") //refer github.com/amit-lulla/twitterapi
	
	var data twitterapi.User
	data, _ = api.GetUsersShow(*handlePtr, nil)
	details, _ := json.MarshalIndent(data, "", " ")
	
	fo, _ := os.Create("./userinfo.txt")
	fo.WriteString(string(details))
	fo.Close()
}