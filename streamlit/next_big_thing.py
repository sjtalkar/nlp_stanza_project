import numpy as np
import pandas as pd
import streamlit as st
import os
from PIL import Image

from pathlib import Path

from nbt_utils import get_wikipedia_search_results, get_stanza_dict_of_first_sentence, get_category_from_search_term, graph_sent, get_first_unambiguous_wiki_term_and_page, get_mvp_terms



# https://stackoverflow.com/questions/69768380/share-streamlit-cant-find-pkl-file
img_path = Path(__file__).parents[1] / 'streamlit/images/NextBigThingHeader.png'
image = Image.open(img_path)


st.image(image, caption='The Thing vs The Thing vs Thing')

st.markdown("""Find the next big thing!!!""")

st.selectbox('Select a Thing', get_mvp_terms())  


#st.write(get_stanza_dict_of_first_sentence("This is a senetce.").text)


nbt_input = st.text_input('Find the next big thing like...', 'type here')

list_of_choices = get_wikipedia_search_results(nbt_input)
list_of_choices.insert(0, 'Select one')
print(list_of_choices)


if nbt_input not in ['type here', '']:

    wiki_selection = st.selectbox(
    'Can you please narrow down your query?',
    list_of_choices)

    st.write('You selected:', wiki_selection)

    if wiki_selection != 'Select one':
        #Get category
        nlp_category_phrase, expanded_year_wiki_cats, best_wiki_cats, first_wiki_term = get_category_from_search_term(wiki_selection)
        first_wiki_term, wiki_page = get_first_unambiguous_wiki_term_and_page(wiki_selection)
        #print(category)

        #Get subreddits

        #Get influencers

        #Get relevant influencers posts

        #Extract relevant phrases to category

        #Select final answer

        #nbt = 'next big thing'


        st.write('"',' '.join(nlp_category_phrase),'"', ' is the NLP category of the next big:', wiki_selection)

        # st.markdown("The first sentence from wikipedia is:", wiki_page.summary)

        st.write("Chase the arrow to expand the image of the word dependencies below. ----->")
        

        

        
     
        st.graphviz_chart(graph_sent(get_stanza_dict_of_first_sentence(wiki_page.summary)), use_container_width=False)

st.write("Being unfamiliar with Reddit prior to this project, we were pretty shocked to realize the depth and reach of Reddit when considering using it for our master’s Capstone project. According to statistics from 2020 found in 10 Reddit Statistics Every Marketer Should Know, there are more than 52 million daily active Reddit users worldwide, many of whom are from the United States. In the US there are nearly 222 million monthly active users and 18% of American adults say they are Reddit users. What differentiates Reddit from other social media networks is its structure around communities, known as subreddits. All conversations on Reddit take place within a community with the intention that all posts and comments focus on the specific topic(s) that the subreddit was created for. This means that if you look at the activity within a subreddit, you can safely assume that it will focus on the content you care about. Reddit has moderators within each subreddit that enforce community rules, such as the type of posts that are and are not allowed, including staying on topic.")

st.write("CRF trained on whole corpus, not indiviudual wiki categories as some are too small, one a few articles")