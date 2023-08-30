import { createStore } from 'vuex';
import axios from '@/axios';


export default createStore({
    state(){
        return {
        movies: [],
        movie:{},
        pagination: {},
        actors: [], 
        };
      },
      
       getters : {
        getMovies: state => state.movies,
      },
      
       actions :{
          async fetchMovies({ commit }, page = 1) {
              try {
                const response = await axios.get(`/api/movies/?page=${page}`);
                commit('setMovies', response.data.results);
                commit('setPagination', response.data);
              } catch (error) {
                console.error('Error fetching movies:', error);
              }
            },
        async fetchMovieById({ commit }, data) {
          try {
            const response = await axios.get(`/api/movies/${data.movieId}/`);
            commit('setMovie', response.data);
          } catch (error) {
            console.error('Error fetching movie by ID:', error);
            return null;
          }
        },
        async fetchActorsFct({ commit }) {
          try {
            const response = await axios.get('/api/actors/');
            commit('setActors', response.data);
          } catch (error) {
            console.error('Error fetching actors:', error);
          }
        },
        async updateMovieRating({ commit, dispatch }, updatedMovie) {
          try {
            const response = await axios.put(`/api/movies/${updatedMovie.id}/`, updatedMovie.movie);
            commit('setMovie', response.data);
            if (updatedMovie.rating) {
              const reviewData = updatedMovie.rating;
              const movieId = updatedMovie.id
              dispatch('addReview', { movieId , reviewData });
            }
          } catch (error) {
            console.error('Error updating movie:', error);
          }
        },
        async addReview({ commit }, { movieId, reviewData }) {
          try {
            const response = await axios.post(`/api/reviews/`, reviewData);
            commit('addReviewToMovie', { movieId, review: response.data });
          } catch (error) {
            console.error('Error adding review:', error);
          }
        },
      },
      
       mutations :{
        setMovies(state, movies) {
          state.movies = movies;
        },
        setMovie(state, movie) {
          state.movie = movie;
        },
        setPagination(state, paginationData) {
          state.pagination = paginationData; // Mutate the pagination data
        },
        setActors(state, actors) {
          state.actors = actors;
        },
    
      },
      
      
});
