# Cat Guru

<p align="center">
  <!-- License -->
  <a href="https://github.com/hrosicka/CatGuru/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/hrosicka/CatGuru?color=blue" alt="License">
  </a>
  <!-- Issues -->
  <a href="https://github.com/hrosicka/CatGuru/issues">
    <img src="https://img.shields.io/github/issues/hrosicka/CatGuru?logo=github" alt="Open Issues">
  </a>
  <!-- Pull Requests -->
  <a href="https://github.com/hrosicka/CatGuru/pulls">
    <img src="https://img.shields.io/github/issues-pr/hrosicka/CatGuru?logo=github" alt="Pull Requests">
  </a>
  <!-- Repo Size -->
  <img src="https://img.shields.io/github/repo-size/hrosicka/CatGuru?color=blueviolet" alt="Repo Size">
  <!-- Last Commit -->
  <img src="https://img.shields.io/github/last-commit/hrosicka/CatGuru?logo=github" alt="Last Commit">
  <!-- Top Language -->
  <img src="https://img.shields.io/github/languages/top/hrosicka/CatGuru?logo=code" alt="Top Language">
  <!-- Stars -->
  <a href="https://github.com/hrosicka/CatGuru/stargazers">
    <img src="https://img.shields.io/github/stars/hrosicka/CatGuru?style=social" alt="Stars">
  </a>
  <!-- Forks -->
  <a href="https://github.com/hrosicka/CatGuru/network/members">
    <img src="https://img.shields.io/github/forks/hrosicka/CatGuru?style=social" alt="Forks">
  </a>
  <!-- Watchers -->
  <a href="https://github.com/hrosicka/CatGuru/watchers">
    <img src="https://img.shields.io/github/watchers/hrosicka/CatGuru?style=social" alt="Watchers">
  </a>
</p>

Bored? Ask Cat Guru for a random cat fact and be amazed! Based on Cat Facts API: https://catfact.ninja/fact

The application was created using the Tkinter framework and icons / pictures using Figma. 

## User Documentation
Cat Guru is a desktop application that generates random cat facts and allows users to change the background and avatar.

## Usage
1. Launch the application.
2. Click the "Ask the Cat Guru" button.
3. Read the cat fact that is displayed.
4. Change the background and avatar to your liking.

## Features
- "Ask the Cat Guru" button: Generates a new cat fact.
  
   ![](https://github.com/hrosicka/CatGuru/blob/master/Doc/CatGuruDoc1.png)
  
- "Change Avatar" button: Allows you to choose a new one avatar.
  
   ![](https://github.com/hrosicka/CatGuru/blob/master/Doc/CatGuruDoc2.png)
  
- "Change Background" button: Allows you to choose a new one background.

   ![](https://github.com/hrosicka/CatGuru/blob/master/Doc/CatGuruDoc3.png)

## Improving Error Handling with Specific Messages
- To provide more informative error messages, the get_cat_fact function handles specific exceptions and return tailored messages. Logging is used. The file cat_guru.log is created.

  ![](https://github.com/hrosicka/CatGuru/blob/master/Doc/FailedConnection.png)
