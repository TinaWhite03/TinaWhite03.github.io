---
layout: default
title: Databases
---

# Enhancement 3: Databases
## CS320 - Software Testing, Automation QA

## Overview

The third artifact is my final project from CS320. The TaskService.java is a class that manages Task objects using a HashMap. Created to demonstrate the service layer functionality for a task management system.

## Why I Chose This Artifact

I selected this artifact to showcase my competency in:
- In-memory data structures
- Database integration
- Scalability principles
- Separation of concerns

The original artifact provided a great foundation in object-oriented programming. The enhancement adds a persistence layer, making the service more robust and production-ready.

## Technologies Used

- **Java** - Core programming language
- **HashMap** - In-memory data structure
- **DAO Pattern** - Data access object architecture
- **Database Integration** - Persistence layer

## Key Enhancements

### Database Persistence Layer

Transformed the service from in-memory storage to database-persistent solution:

**Before:**
- Data stored in HashMap
- Lost when application stopped
- Not scalable

**After:**
- Database persistence
- TaskDAO implementation
- InMemoryTaskDAO fallback
- Scalable architecture

### Separation of Concerns

Implemented proper architectural patterns:
1. **TaskService** - Business logic layer
2. **TaskDAO** - Data access interface
3. **InMemoryTaskDAO** - In-memory implementation
4. **DatabaseTaskDAO** - Database implementation

## Challenges and Solutions

### Challenge: Data Storage Design
**Solution:** Designed the architecture to follow data integration principles while maintaining flexibility for different storage backends.

### Challenge: Maintainability
**Solution:** Created a clear separation between service and data access layers, making the code more maintainable and adaptable.

## Skills Demonstrated

- Database design and integration
- Data access patterns (DAO)
- Object-oriented design
- System architecture
- Scalability planning

## Conclusion

This enhancement demonstrates my ability to adapt existing code to meet new requirements and implement best practices. The improved architecture showcases my understanding of design patterns and their real-world applications.

[← Back to Projects](/projects)
