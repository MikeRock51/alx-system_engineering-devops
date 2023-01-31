#!/usr/bin/env ruby
# Matches the word "School" using regular expression

puts ARGV[0].scan(/S\w{4}l/).join
