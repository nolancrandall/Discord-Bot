*BLACKJACK CODE IS IN MAIN.PY*


Brief summary of this project prompt in your own words

I created a blackjack game within a Discord Bot.


Explanation of what you chose and why, and what “being successful” meant to you

I chose to work on this project since I had already created a game using pygame, and wanted to convert it over to a form that would work in a discord chat channel. My program starts with the buttons used to hit and stay, 
when they are called, they set did_hit or did_stay to true, which is used later in the code to let the player hit and stay. Being successful means creating a fully functional game that has many of the features of an actual game of blackjack


Full explanation of what your program does + any skeleton code

My program first creates the deck of 52 random cards and then appends the first 2 to the player_hand list and the next 2 to the enemy_hand list. When the player hits, I append another card to the player_hand list.
When the player stays, I calculate their total score and then calculate the bot's score, having it draw another card when under 16 points.
I then compare the total score for both and whoever has closer to 21 wins, but if the player goes over, they lose
