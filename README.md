## Question 23

### Input

The Doctor and River Song decide to play a game on a directed acyclic graph G, which has one source s and one sink t.

### Problem

Each player has a token on one of the vertices of G. At the start of the game, The Doctor’s token is on the source vertex s, and River’s token is on the sink vertex t. The players alternate turns, with The Doctor moving first. On each of his turns, the Doctor moves his token forward along a directed edge; on each of her turns, River moves her token backward along a directed edge.
If the two tokens ever meet on the same vertex, River wins the game. (“Hello, Sweetie!”) If the Doctor’s token reaches t or River’s token reaches s before the two tokens meet, then the Doctor wins the game.
Describe and analyze an algorithm to determine who wins this game, assuming both players play perfectly. That is, if the Doctor can win no matter how River moves, then your algorithm should output “Doctor”, and if River can win no matter how the Doctor moves, your algorithm should output “River”. (Why are these the only two possibilities?) The input to your algorithm is the graph G.
