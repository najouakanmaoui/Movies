<template>
  <div class="movie-detail">
    <v-app>
      <v-container>
        <v-card>
          <v-card-text>
            <v-text-field
              v-model="editedMovie.title"
              label="Title"
              outlined
            ></v-text-field>
          </v-card-text>
          <v-card-text>
            <v-text-field
              v-model="editedMovie.description"
              label="Description"
              outlined
            ></v-text-field>
          </v-card-text>
          <v-card-text>
            <strong>Actors</strong>
            <div v-for="actorOption in actorOptions" :key="actorOption.id">
            <label>
              <input
                type="checkbox"
                :value="actorOption.id"
                v-model="editedMovie.actors"
              />
              {{ actorOption.fullName }}
            </label>
          </div>
          </v-card-text>
          <v-card-text>
            <v-slider
              v-model="editedMovie.rating"
              min="1"
              max="5"
              step="1"
              label="Rating"
            ></v-slider>
          </v-card-text>
        </v-card>
        <v-btn @click="updateMovie">Update Movie</v-btn>
        <router-link to="/"><v-btn >Back to Movie List</v-btn></router-link>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import {
  VContainer,
  VCard,
  VCardText,
  VBtn,
  VTextField,
  VSlider,
} from 'vuetify/lib/components';

export default {
  components: {
    VContainer,
    VCard,
    VCardText,
    VBtn,
    VTextField,
    VSlider,
  },
  computed: {
    movie() {
      return this.$store.state.movie;
    },
    actors() {
      return this.$store.state.actors;
    },
    actorOptions() {
      return this.actors.map(actor => ({
        id: actor.id,
        fullName: `${actor.first_name} ${actor.last_name}`,
      }));
    },
    
  },
  data() {
    return {
      editedMovie: {
        title: '',
        description: '',
        actors: [],
        rating: 5,
      },
    };
  },
  mounted() {
    this.getMovie();
    this.fetchActors();
  },
  methods: {
    ...mapActions(['updateMovieRating', 'fetchMovieById', 'fetchActorsFct']),
    updateMovie() {
      const updatedMovie = {
        id: this.movie.id,
        movie: {
          title: this.editedMovie.title,
          description: this.editedMovie.description,
        },
        rating: {
          movie: this.movie.id,
          grade: this.editedMovie.rating,
        },
      };
      if (this.editedMovie.actors.length > 0) {
        updatedMovie.movie.actors = this.editedMovie.actors;
      }
      this.updateMovieRating(updatedMovie);
    },
    getMovie() {
      this.fetchMovieById({ movieId: this.$route.params.movieId }).then(() => {
        this.editedMovie.title = this.movie.title;
        this.editedMovie.description = this.movie.description;
        this.editedMovie.actors = this.movie.actors.map(actor => actor.id);
        this.editedMovie.rating = this.movie.average_reviews || 5;
      });
    },
    fetchActors() {
      this.fetchActorsFct();
    },
  },
};
</script>

<style scoped>
.movie-detail {
  padding: 20px;
}

.movie-title {
  font-size: 24px;
  margin-bottom: 20px;
}

.actors-list {
  list-style: none;
  padding-left: 0;
}

</style>
