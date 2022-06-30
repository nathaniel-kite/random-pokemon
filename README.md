# random-pokemon
Generates a list of random pokemon, either automatically or through a one-person draft.

For a draft, do:
`python random_poke.py draft` or `python random_poke.py d`

For just a random list, do:
`python random_poke.py random` or `python random_poke.py r`

By default, the program generates either 18 random pokemon, or a draft with 8 rounds and 4 options per  round. If you'd like, you can change these by modifying the constants in `random_poke.py`. You can also change the list of pokemon to choose from, provided you have a new file to replace it with.

###### Here are my preferred rules for drafting:
- Build teams as National Dex AG
- Double Battles
- No Mythical or Restricted Pokemon
- Endless Battle Clause (no causing infinite battles)
- Evasion Clause (no Double Team or Minimize)
- Gravity Sleep Clause (No Gravity + a sleep move with < 100% accuracy)
- No Z-Moves, Megas, or Dynamax
- Notably, no species clause! If you draft a pokemon twice, you can use it twice!
- If the pokemon is in Gen 8, it uses its Gen 8 abilities, stats, etc.
- If the pokemon is not in Gen 8, it only has access to moves that exist in Gen 8

###### Notably unavailable moves:
- Frustration
- Heal Order
- Hidden Power
- Pursuit
- Return
- Signal Beam
- Spotlight
- Tail Glow

(See https://www.serebii.net/swordshield/unusableattacks.shtml for all unusable moves in Gen 8)
