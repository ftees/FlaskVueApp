import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../pages/LoginPage.vue';
import RegisterPage from '../pages/RegisterPage.vue';
import UploadTrainingPage from '../pages/UploadTrainingPage.vue';

const routes = [
  { path: '/', component: LoginPage },
  { path: '/login', component: LoginPage },
  { path: '/register', component: RegisterPage },
  { path: '/training', component: UploadTrainingPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
