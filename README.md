# Card game bot for discord (name to be decided)
This game consists of a set of rules for creating your own cards,
each player contributes to the set of cards in a game,
The current theme for the card game is: *Middle Age*
There are 2 types of cards in the game, unit cards and effect cards,
unit cards represent entities that can deal damage and have health.

## Creating cards:
This game has a rarity system that limits the amount of strong cards
the overall deck can have, the rarer the card the stronger it is.
The amount of cards in a deck is calculated by the bot, it can add
or remove cards in order to satisfy the rarity mechanism.

Rarity:
55% of the deck are composed by common cards,
25% of the deck are composed by uncommon cards,
15% of the deck are composed by rare cards,
5% of the deck are composed by epic cards.

Before starting the game, each player has to create a set of cards
for the game, at maximum each player can only create:
* 11 common cards
* 5 uncommon cards
* 3 rare cards
* 1 epic card

### Card types
This game have 2 types of cards, unit cards and effect cards,
unit cards can have effects but **only** if they have a
**fair** condition to activate it, those effects are so
called *Skills* and abide to the effect card rules, effect cards
can affect health, damage and money (price and player money),
effect cards can only effect units, not being able to increase
others effects status.

This game has three status types, price, health and damage.
Price is the amount of money a player pays to acquire a card on
the buying cycle of the game.
Health of a unit represent it's life, if it reaches 0 the card
goes back to the game deck.
Damage is dealth by units and decrease the amount of health of
the opponent unit card.

The amount of health, price and damage each card can have are
inversely proportional to it's rarity.

### Rules for creating unit cards
Price, health and damage are directly proportional to the rarity,
those status types can vary a little bit obeying the table bellow:
Rarity | Price | Health | Damage
--- | --- | --- | ---
Common (55%) | from $1 to $10 | 1❤ to 5❤ | 0♠ to 5♠
Uncommon (25%) | from $10 to $20 | 5❤ to 10❤ | 5♠ to 10♠
Rare (15%) | from $20 to $40 | 10❤ to 20❤ | 10♠ to 20♠
Epic (5%) | from 40$ to 80$ | 20❤ to 40❤ | 20♠ to 40♠

### Rules for creating effect cards
Effect cards are used to affect unit cards, it's effect are also
directly proportional to the rarity, rarer the card stronger is it's effect.

Rarity | Price | Effect
--- | --- | ---
Common (55%) | from $1 to $10 | affects at maximum 5% of health, money or damage
Uncommon (25%) | from $10 to $20 | affects at maximum 10% of health, money or damage
Rare (15%) | from $20 to $40 | affects at maximum 20% of health, money or damage
Epic (5%) | from 40$ to 80$ | affects at maximum 40% of health, money or damage

Notice: *Effect cards rules are still under development*

## Gameplay

TO-DO