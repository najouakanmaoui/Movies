import { createRouter, createWebHistory } from 'vue-router';
import MoviesList from '@/components/MoviesList.vue';
import MovieDetail from '@/components/MovieDetail.vue'; 

const routes = [
  { path: '/', component: MoviesList },
  { path: '/movie/:movieId', component: MovieDetail, props: true }, 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
