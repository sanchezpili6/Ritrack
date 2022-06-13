import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from "@/views/LoginView";
import SignUpView from "@/views/SignUpView";
import LostView from "@/views/LostView";
import FoundView from "@/views/FoundView";
import ProfileView from "@/views/ProfileView";
import MyPetsView from "@/views/MyPetsView";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'sign up',
    component: SignUpView
  },
  {
    path: '/lost',
    name: 'lost',
    component: LostView
  },
  {
    path: '/found',
    name: 'found',
    component: FoundView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/my-pets',
    name: 'my pets',
    component: MyPetsView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
