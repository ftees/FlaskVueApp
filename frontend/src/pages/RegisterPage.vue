<template>
  <div class="register-container">
    <v-sheet width="300" class="mx-auto">
      <v-form @submit.prevent @submit="register">
        <p>Account</p>
        <v-text-field
          v-model="firstName"
          type="input"
          :rules="rules"
          label="First name"
        ></v-text-field>
        <p>Password</p>
        <v-text-field
          v-model="password"
          label="Password"
          :rules="rules"
          type="input"
          hint="Enter your password to access this website"
        ></v-text-field>
        <v-text-field
          v-model="confirmPassword"
          label="Password"
          :rules="rules"
          type="input"
          hint="Enter your password to access this website"
        ></v-text-field>
        <v-btn type="submit" block class="mt-2 btn-login">LOG IN</v-btn>
      </v-form>
    </v-sheet>
    <a href="/login">Login now ></a>
  </div>
</template>

<script>
import router from '@/router';

export default {
  data: () => ({
    firstName: '',
    password: '',
    confirmPassword: '',
    rules: [
      (value) => {
        if (value) return true;
        return 'You must input this field.';
      },
    ],
  }),
  methods: {
    register() {
      if (this.password !== this.confirmPassword) {
        alert('Password and confirm password must be the same');
        return;
      }
      fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.firstName,
          password: this.password,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data) {
            router.push('/login');
          } else {
            alert('Login failed');
          }
        });
    },
  },
};
</script>
<style scoped>
.register-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: center;
  align-items: center;
  height: 500px;
  margin-top: 20px;
  background-color: #ffffff;
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
  border: 1px solid #e3e3e3;
  border-radius: 10px;
}

a {
  color: #48bdf0;
  text-decoration: none;
}

.btn-login {
  background-color: #8fc7f2;
  color: #3282bf;
}
</style>
