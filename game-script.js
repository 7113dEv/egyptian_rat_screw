// window.onload = () => {
//   addEventHanders();
// };

// Create Deck
const createDeck = (numberOfCards) => {
    let deck = [];
    const suits = ["Spades", "Clubs", "Hearts", "Diamonds"];
    for (let suit of suits) {
        let card = [suit, 0];
        for (let i = 1; 1 <= numberOfCards; i++) {
            card[1] = i;
            deck.push(card);
        }
    }
    console.log(deck);
};

// Deal Deck to each player
// Players flip cards over in order
// If Royal or Ace is turned over, begin Rat Screw
// If player cannot answer the screw, previous player gets all cards flipped