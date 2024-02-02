<template>
  <form @submit.prevent="submitForm">
    <v-text-field v-model="formData.token" label="token"></v-text-field>

    <v-btn class="me-4" type="submit"> submit </v-btn>
  </form>

  <p>{{ pred }}</p>
  <img v-if="chartImage" :src="chartImage" alt="K-Means Chart" />
</template>

<script>
export default {
  data() {
    return {
      formData: {
        token: '',
      },
      pred: '',
      chartImage: '',
    };
  },
  methods: {
    submitForm() {
      fetch('/api/predict/' + this.formData.token, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify(this.formData),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log('Server Response:', data);
          this.pred = data['prediction'];
          this.chartImage = `data:image/png;base64, ${data.chart_image}`;
        })
        .catch((error) => {
          console.error('Error:', error);
          this.pred = error;
        });
    },
  },
};
</script>

<style scoped>
p {
  margin: 20px;
}
</style>
