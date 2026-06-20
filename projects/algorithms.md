---
layout: default
title: Algorithms & Data Structures
---

# Enhancement 2: Algorithms and Data Structures
## CS330 - Computational Graphics and Visualization

The second artifact is the final project from my CS 330 class, Computational Graphics and Visualization course. Created in the Winter of 2025, it's a C++ application that uses OpenGL and GLFW for rendering a 3D scene. The project has classes named ViewManager, SceneManager, and Camera to manage the 3D environment, lighting, textures, and shapes to make a living room scene with a television, carpeted flooring, and lighting. 

I chose this artifact because it showed my compentency of my ability to work with graphical programming. With the intial version of the code it's functional and rendered eveI rything in the scene just fine the enhancement I implemented was an octree partitioning system I was able to improve the algorithms with the improvements I was able to demonstrate my ability to find and analyze the system weakness and applied the solution to reduce the workload of the rendering, greatly improving the performance and effeciency highlighting my growth.

My initial task was to analyze the original code and find the problem with why it isn't running efficiently. I found that the RenderScene in SceneManager.cpp called the m_basicMeshes-> and the DrawBoxMesh had similar functions for the objects and frame. Improving this, I made the Octree, which made the 3D space into eight octants. The hardest challenge was to integrate it into the existing rendering, as it's something separate from the scene. This taught me the importance of balancing the algorithms with practical implementation. I can say that I met the credentials of Outcomes 3 and 4 with the enhancement. By providing the evidence of my improvements, I can confidently say that I achieved the results in a meaningful way.

[Original]

[Enhancement]

[← Home Page](https://tinawhite03.github.io/projects)
