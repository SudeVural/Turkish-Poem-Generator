# Turkish Poem Generator
 A poem generator that uses an N-gram language model.  

The generator is still incomplete. Our models mostly work but they do not meet our initial goals.
Bigram model is complete. However, since it is a bigram model it is rather meaningless for a poem. Though, this is what we have expected at the beginning.
Our trigram model works fine but there are some oddnesses. We are not sure at this point if they are caused by our data being too small for a trigram model or we lack something in our code (such as; start and end tokens, or a bug in our code).
We added start and end tokens when we were tokenizing but they caused some problems, so at this point we do not have them.
We implemented a different function for the first verses. It works fine for the bigram model, but the first verse in the trigram model has some problems to be fixed.

We have some ideas that we did not yet have a chance to code. We tried a basic version of this in the code but it does not work. We want to limit which words can occur at the end of a line by implementing a code (probably with start and end tokens). 
