<template>
  <form @submit.prevent="submitForm">

    <v-select
      v-model="formData.model"
      :items="items"
      label="Model"
    ></v-select>

    <v-text-field
      v-model="formData.clusters"
      label="Clusters"
    ></v-text-field>

    <v-btn
      class="me-4"
      type="submit"
    >
      submit
    </v-btn>

  </form>

  <p>Token : {{ r }}</p>

</template>

<script>

export default {
  data() {
    return {
      formData: {
        model: '',
        clusters: '',
      },
      items: [
        "K-means",
        "XGBoost"
      ],
      r: ''
    };
  },
  methods: {
    submitForm() {
      fetch(`/api/train`, {method: "POST", headers: {'content-type': 'application/json'}, body: JSON.stringify(this.formData) })
        .then(response => response.json())
        .then(data => {
          console.log('Server Response:', data);
          this.r = data['token']
        })
        .catch(error => {
          console.error('Error:', error);
          this.r = error
        });
    },
  },
};
</script>

<style scoped>

</style>
