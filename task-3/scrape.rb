require 'nokogiri'
require 'open-uri'

puts "search for: "
key = gets.chomp
page1 = Nokogiri::HTML(open("https://www.google.com/search?q=#{key}&client=ubuntu&hs=Gkv&channel=fs&ei=t9v4XY6HB4nUz7sP57uhmAk&start=0&sa=N&ved=2ahUKEwjOvtu06LzmAhUJ6nMBHeddCJMQ8tMDegQIExAv&biw=1853&bih=951"))
page2 = Nokogiri::HTML(open("https://www.google.com/search?q=#{key}&client=ubuntu&hs=Gkv&channel=fs&ei=t9v4XY6HB4nUz7sP57uhmAk&start=10&sa=N&ved=2ahUKEwjOvtu06LzmAhUJ6nMBHeddCJMQ8tMDegQIExAv&biw=1853&bih=951"))
title1 = page1.css('div.vvjwJb')
title2 = page2.css('div.vvjwJb')
url1 = page1.css('div.BNeawe.UPmit.AP7Wnd')
url2 = page2.css('div.BNeawe.UPmit.AP7Wnd')
title = title1 + title2
url = url1 + url2
for i in (0..9)
	puts title[i].text
	puts url[i].text
	puts " "
end
