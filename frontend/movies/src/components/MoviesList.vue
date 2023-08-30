<template>
  <div class="movie-list">
    <v-app>
      <v-container>
        <h1 class="headline">Movie List</h1>
        <v-row class="movie-row">
          <v-col
            v-for="movie in movies"
            :key="movie.id"
            cols="6"
            md="2"
          >
            <v-card class="movie-card" @click="goToEditPage(movie.id)">
              <v-card-title class="movie-title">{{ movie.title }}</v-card-title>
              <v-card-text class="movie-description">
                {{ movie.description }}
              </v-card-text>
              <v-card-text>
                <strong>Actors:</strong>
                <ul class="actors-list">
                  <li v-for="actor in movie.actors" :key="actor.id">
                    {{ actor.first_name }} {{ actor.last_name }}
                  </li>
                </ul>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
       <v-pagination
          v-if="pagination"
          v-model="currentPage"
          :length="pagination.total_pages"
          @input="loadPage"
          class="pagination"
        >
          <template #prev>
            <v-btn
              color="primary" 
              text
              :disabled="pagination.next"
              rounded
              class="pagination-button"
              @click="prevPage"
            >
              Prev
            </v-btn>
          </template>
          <template #next>
            <v-btn
              color="primary"
              :disabled="pagination.previous"
              text
              rounded
              class="pagination-button"
              @click="nextPage"
            >
              Next
            </v-btn>
          </template>
        </v-pagination>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import {
  VApp,
  VBtn,
  VContainer,
  VRow,
  VCol,
  VCard,
  VCardTitle,
  VCardText,
  VPagination,
} from 'vuetify/lib/components';

export default {
  components: {
    VApp,
    VBtn,
    VContainer,
    VRow,
    VCol,
    VCard,
    VCardTitle,
    VCardText,
    VPagination,
  },
  data() {
    return {
      currentPage: 1,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    pagination() {
      return this.$store.state.pagination;
    },
  },
  mounted() {
    this.loadMovies();
  },
  methods: {
    ...mapActions(['fetchMovies']),
    loadMovies(page = 1) {
      this.currentPage = page;
      this.fetchMovies(page);
    },
    loadPage(page) {
      this.loadMovies(page);
    },
    goToEditPage(movieId) {
      this.$router.push({ path: `/movie/${movieId}` });
    },
    prevPage() {
      if (this.pagination.previous) {
        this.loadPage(this.currentPage - 1);
      }
    },

    nextPage() {
      if (this.pagination.next) {
        this.loadPage(this.currentPage + 1);
      }
    }

  },
};
</script>

<style scoped>
.movie-list {
  padding: 20px;
}

.headline {
  font-size: 24px;
  margin-bottom: 20px;
}

.movie-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.movie-card {
  cursor: pointer;
  margin-bottom: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s, box-shadow 0.3s;
}

.movie-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.pagination button:focus {
  outline: none;
}

.v-pagination__item {
  color: #1976D2;
}

.v-pagination__item--active {
  background-color: #1976D2;
  color: white;
  border-color: #1976D2;
}
</style>
