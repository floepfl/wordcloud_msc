## User caveats
1. **Order of words in .csv file matters**: the algorithm starts by filling in available space choosing big fonts with the first words in the .csv file (starting from above)
2. **Works better with image of colored shapes**:
3. ****:
4. ****:


## Developer caveats
1. **`enable_events` for save as `Button` requires invisible `Input` box**: see https://github.com/PySimpleGUI/PySimpleGUI/issues/3143
2. **Cannot make `FileSaveAs` invisible**: manually configured it using a `Button` whereas it is discouraged by PySimpleGUI documentation 
3. install_name_tool -change @rpath/libiomp5.dylib /Users/civiliste/PycharmProjects/wordcloud_app/dist/main/libiomp5.dylib libmkl_intel_thread.1.dylib
