# Spotify-based Recommender Bot
This repo contains a source code for Telegram Bot where the music recommendation system is deployed. The recommendations are based on the unique tracks chacacteristics (like loudness and danceability) computed by Spotify.

#### -- Project Status: Completed

## Intro

The main goal of the project is to create a system that takes track and its author and returns N most similar tracks. Similarity is based on the cosine distance between vector represenation of the tracks. 

### Techniques Used
* Parsing
* Tracks similarity
* Recommendation system
* Telegram Bot

### Technologies
* Python
* Telebot
* Spotify API

## Methodology

The process of creating the bot was as follows:

1. Create a list of artists to parse
2. Parse the data
3. Clusterization
4. Similarity matrix 
5. Recommendations

To create a database of tracks to recommend from, I created a list of artists by each decade starting from 1950s. Thus, all periods of music development are considered by the bot. Then, to enhance the similarities, tracks are vectorized and clusterized. Finally, the bot returns top N tracks that are the closest to the input track by cosine similarity. 

## Installation

1. Clone this repo: 

`git clone https://github.com/Pavel-Polyanskiy/Spotify-based-bot-recommender`

2. Download the [**data**](https://drive.google.com/drive/folders/1kGO7RDblhRLDrqITp1lAbEHk8w0Shqdm?usp=share_link) folder ( the files are not uploaded in Github due to the size limits)

3. Run `telegram_bot.ipynb` 

4. Find `@Spotikbot_bot` in Telegram search and start using!

5. Sample outputs


<p align="center">
      <img width="381" alt="Screenshot 2023-03-03 at 14 29 48" src="https://user-images.githubusercontent.com/84684422/222746514-2718e758-fa71-4103-82fb-ab59f6bcb986.png">
 </p>
 <p align="center">
     <img width="381" alt="Screenshot 2023-03-03 at 14 30 03" src="https://user-images.githubusercontent.com/84684422/222746519-949b9d16-e3ab-4770-9c95-6e0540200d03.png">
</p>


<p>

## Contact
✉️ pavelpolyanskiyhse@gmail.com
</p>
