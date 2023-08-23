<!-- TrainingCourses.vue -->
<template>
  <div>
    <!-- JarWare Developer: Display a list of training courses -->
    <h1>Training Courses</h1>
    <ul>
      <li><router-link to="/purchase-training">Purchase Training</router-link></li>
      <li><router-link to="/travel-training">Travel Training</router-link></li>
      <!-- ...other course links -->
    </ul>
  </div>
</template>

<!-- PurchaseTraining.vue -->
<template>
  <div>
    <!-- JarWare Developer: Display purchase training details and quiz submission button -->
    <h2>Purchase Training for Card Holders</h2>
    <p>Complete the quiz to earn your certificate.</p>
    <button @click="submitQuiz">Submit Quiz</button>
  </div>
</template>

<script>
export default {
  methods: {
    submitQuiz() {
      // JarWare Developer: Simulate quiz submission and certificate issuance
      setTimeout(() => {
        alert('Congratulations! You have completed the quiz.');
      }, 1000);
    },
  },
};
</script>
