
name: "CodeQL"

on:
  push:
    branches: [ "main" ]
  pull_request:
    # The branches below must be a subset of the branches above
    branches: [ "main" ]
  schedule:
    - cron: '32 2 * * 2'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'python' ]
      
    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    # Initializes the CodeQL tools for scanning.
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v2
      with:
        languages: ${{ matrix.language }}
      
      uses: github/codeql-action/autobuild@v2

  

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v2
      with:
        category: "/language:${{matrix.language}}"





answer = input("do you want to play (yes/no) ?")

if answer.lower().strip() == "yes":

    answer = input("you reach a crossroads, do you want to go left or right? ").lower().strip()
    if answer == "left":
        answer = input("you encounter a monster, do you want to fight or run? ").lower().strip()

        if answer == "fight":
            print("the monster fights back and kills you (bad ending 1) ")

        elif answer == "run":
            answer = input("do you want to go into the forest?(yes/no) ")

            if answer == "yes":
                print("you got lost and drowned in the river (bad ending 2) ")
            elif answer == "no":
                answer = input("you see a town nearby, do you want to go there (yes/no) ")

                if answer == "yes":
                    print("you decided to live here(good ending 1) ")
                elif answer == "no":
                    answer = input("you decided to go on the opposite path, but suddenly you see a bear, do you want do fight or run" )
                    

    elif answer == "right":
        print("you fall off a cliff and die (bad ending 3) ")

    else:
        print("you lost" )

else:
    print("bye!" )
