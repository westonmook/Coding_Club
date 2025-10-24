#include <iostream>
auto yn = 'b';
int yloop() {
  for(int i = 0; i < 100; i++) {
    std::cin >> yn;
    if(yn == 'y' || yn == 'n') {
      break;
  return 0;
    }
  }
}

int main() {
  std::string test = "Why aren't you Coding?\n";
  std::cout << test;
  yloop();
  if(yn == 'I am!') {
    std::cout << "Good choice. \n" << "The future will rely on the tech-makers.\n";
    int pchoice = 0;
    std::cin >> pchoice;
    if(pchoice == 1) {
      std::cout << "The apple appears in your hand. it seems to flash in and out of existence. The screen just in front of the merchants eyes flashes for roughly 15 seconds before he says. Thank you for your purchase. He fades from your presence\n";
    }}}

//rock beats scissors
//rock beats lizard
//paper beats rock
//paper beats spock
//scissors beats paper
//scissors beats lizard
//lizard beats paper
//lizard beats spock
//spock beats rock
//spock beats scissors
#include <iostream>
#include <stdlib.h>

int main(){
  srand (time(NULL));
  int c = rand() % 5 + 1;
  int u = 0;
  std::string comp = " The computer beat you.";
  std::string use = " User wins!";
  //menu
  std::cout << "__________________" << "\nRock, Paper, Scissors, Lizard, Spock\n" << "==================\n";
  std::cout << "Enter a number 1-5 ex. 4\n";
  std::cout << "1. Rock\n" << "2. Paper\n" << "3. Scissors\n" << "4. Lizard\n" << "5. Spock\n";
  std::cin >> u;
  //logic
  if (u == 1 && c == 2) {
    std::cout << "Paper beats rock. The computer beat you.";
  } else if (u == 1 && c == 3) {
    std::cout << "Rock beats Scissors. User wins!";
  } else if (u == 1 && c == 4) {
    std::cout << "Rock beats Lizard. User wins!";
  } else if (u == 1 && c == 5) {
    std::cout << "Spock blasts rock. The computer beat you.";
  } else if (u == 2 && c == 1) {
    std::cout << "Paper covers Rock. User wins!";
  } else if (u == 2 && c == 3) {
    std::cout << "Scissors cut paper. The computer beat you.";
  } else if (u == 2 && c == 4) {
    std::cout << "Lizard eats paper. The computer beat you.";
  } else if (u == 2 && c == 5) {
    std::cout << "Spock hates paperwork. User wins!";
  } else if (u == 3 && c == 1) {
    std::cout << "Rock crushes scissors. The computer beat you.";
  } else if (u == 3 && c == 2) {
    std::cout << "Scissors cut paper. User wins!";
  } else if (u == 3 && c == 4) {
    std::cout << "Scissors slice Lizard. User wins!";
  } else if (u == 3 && c == 5) {
    std::cout << "Spock crushes scissors. The computer beat you.";
  } else if (u == 4 && c == 1) {
    std::cout << "Rock beats lizard." << comp;
  } else if (u == 4 && c == 2) {
    std::cout << "Lizard eats paper." << use;
  } else if (u == 4 && c == 3) {
    std::cout << "Scissors slice Lizard." << comp;
  } else if (u == 4 && c == 5) {
    std::cout << "Lizard poisons Spock." << use;
  } else if (u == 5 && c == 1) {
    std::cout << "Spock blasts rock." << use;
  } else if (u == 5 && c == 2) {
    std::cout << "Spock hates paperwork." << comp;
  } else if (u == 5 && c == 3) {
    std::cout << "Spock crushes scissors." << use;
  } else if (u == 5 && c == 4) {
    std::cout << "Spock gets poisoned by the lizard." << comp;
  } else if (u == c) {
    std::cout << "An epic battle takes place but because of my poor variable assignment we won't only you know what is fighting what. either way, Tie. Try again.";
  }
}