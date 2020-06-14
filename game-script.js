// window.onload = () => {
//   addEventHanders();
// };

//Create Deck
const createDeck = () => {
    let deck = [];
    let suits = ['Spades', 'Clubs', 'Hearts', 'diamonds'];
    for (let suit of suits) {
        let cardsToAdd = [];
        let card = [0, suit];
        for (let i = 1; i < 14; i++) {
            card = [i, suit];
            cardsToAdd.push(card);
        }
        deck.push(cardsToAdd);
    }
    return deck;
}

// Deal Deck to each player
const createPlayers = (NumOfPlayers) => {
        switch (NumOfPlayers) {
            case 3:

                break;
            case 4:

                break;
            case 5:

                break;
            default:
                break;
        }

        // Players flip cards over in order
        // If Royal or Ace is turned over, begin Rat Screw
        // If player cannot answer the screw, previous player gets all cards flipped

        const playEjap = (NumOfPlayers) => {
            createDeck();
        }