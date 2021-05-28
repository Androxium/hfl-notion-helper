# hfl-notion-helper

This project was to make completing _Homework For Life_ as part of the Storyworthy journey by Matthew Dicks. 
These scripts allows you to add your daily entry to a Notion workspace.

## Setup
- Follow the offical Notion developer docs [here](https://developers.notion.com/docs/getting-started) to get the integration set up.
- Clone this repo
- Create a `.env` file within this project directory with the following strucutre
```
DB_ID=<YOUR NOTION DB ID>
TOKEN=<YOUR NOTION INTEGRATION AUTH TOKEN>
```
- Make the `hfl` bash script executable by running `chmod +x hfl`
- To allow for the `hfl` script to be executed anywhere, follow [this guide](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7) on 
setting up your path environment

## Usage
Simply run `hfl 'your log entry'`. NOTE the importance of `'`. Using `"` will cause bash to interpret special characters within your input.
