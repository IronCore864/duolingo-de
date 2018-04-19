# List All Your Duolingo Learned Words

by Categories, with English meanings translated by Duolingo.

## Why

While I was starting to learn Estonian one and a half year ago, I was lucky enough to have a very good Estonian language teacher.

She gave us each an empty notebook, with categories predefined, such as verb, adj, food, etc; just like the lessons arranged in Duolingo. So when we learned some new words we could add them under the corresponding category.

In this case, any time when you want to review and enhance, you can choose a category to do so, since somehow they are related and it makes sense to do it by category rather than dictionary order.

This is what exactly Duolingo lacks right now: you can only browse your learned word list order by last reviewed time.

If you want to go over all the words of a certain category you will have to open the class then do all the lessons again, which is inefficient since you are already familiar with most of them and you only forget some of them so you need to do a lot of clicks just to find some certain word you are not sure about.

It would be best if duolingo could provide this feature.

I posted this on the forum of duolingo and hopefully they would agree with me and implement the feature in the near future.

For now, you can just use my script to do so.

## What is it

In a word, it gets all your learned words then order them by categories and generate a word list, with English translations and translated by Duolingo.

## How to use

Install dependencies:

`pip3 install requests`

First, put your account user name and password in the main.py; then simply just run:

`python3 main.py`

Which will generate an `output` file containing the word list sorted by categories.

## Dependency

Python, requests.

## Example Output

See file `output`
