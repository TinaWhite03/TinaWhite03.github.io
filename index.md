---
layout: default
title: ePortfolio
---

# Welcome to My ePortfolio

<!-- TABS -->
<div class="tab-container">
  <div class="tab-labels">
    <span class="tab-label active" onclick="switchTab(event, 'tab1')">📁 Projects</span>
    <span class="tab-label" onclick="switchTab(event, 'tab2')">📊 Skills</span>
    <span class="tab-label" onclick="switchTab(event, 'tab3')">📝 Blog</span>
  </div>
  
  <div id="tab1" class="tab-content active">
    <h3>My Projects</h3>
    <ul>
      <li><strong>Project A</strong> - Description of project A</li>
      <li><strong>Project B</strong> - Description of project B</li>
      <li><strong>Project C</strong> - Description of project C</li>
    </ul>
  </div>
  
  <div id="tab2" class="tab-content">
    <h3>Skills & Expertise</h3>
    <ul>
      <li>JavaScript / TypeScript</li>
      <li>Python & Django</li>
      <li>React & Vue.js</li>
      <li>DevOps & AWS</li>
    </ul>
  </div>
  
  <div id="tab3" class="tab-content">
    <h3>Recent Blog Posts</h3>
    <ul>
      <li><a href="#">How to Build a Portfolio</a></li>
      <li><a href="#">10 Tips for Better Code</a></li>
      <li><a href="#">My Journey in Tech</a></li>
    </ul>
  </div>
</div>

<script>
function switchTab(event, tabId) {
  const container = event.target.closest('.tab-container');
  const contents = container.querySelectorAll('.tab-content');
  const labels = container.querySelectorAll('.tab-label');
  
  contents.forEach(content => content.classList.remove('active'));
  labels.forEach(label => label.classList.remove('active'));
  
  document.getElementById(tabId).classList.add('active');
  event.target.classList.add('active');
}
</script>

## More About Me

This content appears below the tabs.
