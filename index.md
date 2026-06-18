---
layout: default
---

# Welcome to My ePortfolio

Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

<!-- ===== TABS SECTION ===== -->
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
    <p>You can also add <a href="#">links</a> and other content inside tabs.</p>
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
<!-- ===== END TABS ===== -->

## Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
