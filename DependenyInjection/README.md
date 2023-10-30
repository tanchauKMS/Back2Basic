# Dependency Injection

## What is Dependency Injection ? 
There are plenty of definition can be found in the internet and most of them quite hard to understand.

For me, Dependency Injection is the design pattern in which an object or function receives other objects or functions that it requires, as opposed to creating them internally. 



## How can we implement this ? 
There are 3 ways to implement `Dependency Injection` 

1. **Construtor Injection:** Dependencies are provided through the class constructor 

```java
public class MyClass {
    private Dependency dependency;

    public MyClass(Dependency dependency) {
        this.dependency = dependency;
    }
}
```
2. **Setter Injection:** Dependencies are provided through setter methods.
```java
public class MyClass {
    private Dependency dependency;

    public void setDependency(Dependency dependency) {
        this.dependency = dependency;
    }
}
```
3. **Method Injection:** We implements an interface which declares the method(s) to supply the dependency and the injector uses this interface to supply the dependency to the  class.
```java
public interface DependencyInjector {
    void injectDependency(Dependency dependency);
}

public class MyClass implements DependencyInjector {
    private Dependency dependency;

    @Override
    public void injectDependency(Dependency dependency) {
        this.dependency = dependency;
    }
}
```
## The idea of it 

When you want to inherit or use some model 

## Why we need to do this ?

