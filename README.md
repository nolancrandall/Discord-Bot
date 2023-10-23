*BLACKJACK CODE IS IN MAIN.PY*

I created a blackjack game within a Discord Bot. I chose to work on this porject since I had already created a game using pygame, and wanted to convert it over to a form that would work in a discord chat channel. My program starts with the buttons used to hit and stay, 
when they are called, they set did_hit or did_stay to true, which is used later in the code to let the player hit and stay.

There are a lot of other commands that my bot does that are not related to blackjack. the blackjack command starts at line 231

I used my pygame blackjack code as the base for this code, so there are still some lines relating to pygame and images that are not relevant to the current code. 

My program first creates the deck of 52 random cards and then appends the first 2 to the player_hand list and the next 2 to the enemy_hand list. When the player hits, I append another card to the player_hand list.
When the player stays, I calculate their total score and then caclutate the bot's score, having it draw another card when under 16 points.
I then compare the total score for both and whoever has closer to 21 wins, but if the player goes over, they lose
